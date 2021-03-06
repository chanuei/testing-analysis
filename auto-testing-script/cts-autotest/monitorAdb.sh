#!/bin/bash -ux
pid=$1 
ip=$2
resultFold=$3
testcase=$4
maxTime=$5 
r_v=$6
count=0
while true
do
    #ps -axu | grep $pid | grep $testcase
    ps -p $pid
    if [ $? -eq 0 ];then
        count=$(($count+1))
        sleep 60
    else 
        break
    fi 
    if [ "$count" == "$maxTime" ];then
        adb devices | grep $ip 
        if [ $? -ne 0 ];then
            adb connect $ip 
            if [ $? -ne 0 ];then
                echo "adb devices cannot found,wait the machine reboot by itself,after 600 second connect again,testcase: $testcase" >> $resultFold/errorResult
                sleep 600
                adb connect $ip
                if [ $? -ne 0 ];then
                    echo "reboot failed,stop test,testcase: $testcase" >> $resultFold/errorResult 
                    if [ $r_v == "v" ];then
                        echo cp raw
                        cd $localpwd
                        cp ../../../android_x86.backup.raw $disk_path
                        python sendEmail.py "something went wrong while run $testType test in QEMU, testcase is $testcase"
                    else 
                        echo send email
                        python sendEmail.py "something went wrong while run $testType test in $host, ip is $ip, testcase is $testcase , please reboot it"
                    fi
                    exit 1
                fi
            fi
        fi 
        kill $pid 
        break
    fi 
done
