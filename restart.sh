port=8098
pid=`lsof -t -i:$port`
if [ $pid ];then
    kill -9 $pid
fi
nohup python3 manage.py runserver 0.0.0.0:$port &
