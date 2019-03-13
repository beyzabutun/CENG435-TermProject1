# CENG435-TermProject1
Data Communication and Networking


Beyza Bütün
Soner Durmaz


Please use python 2.7.6

Experiment 1:

1.) open five different ssh connection to geni, which are source, broker, router1, router2, and destination.

2.) copy each of our node's code to their geni connection (our code is with .py extension, and their name is nodes name so consider this while copying it to geni servers)

3.) copy ntplib.py, which is a open source python library, to source and destination's ssh connection. (We also send you ntplib.py with our submission)
3.) in broker, router1, router2 and destination's (source not included) ssh connection, type terminal 'sudo tc qdisc add dev eth0 root netem delay 1ms 5ms', 'sudo tc qdisc add dev eth1 root netem delay 1ms 5ms', 'sudo tc qdisc add dev eth2 root netem delay 1ms 5ms' and also for only broker type 'sudo tc qdisc add dev eth3 root netem delay 1ms 5ms'
3.) in connection of source node; type to terminal 'python source.py' in python, in connection of broker node; type to terminal 'python broker.py', in connection of router1 node; type to terminal 'python router1.py', in connection of router2 node; type to terminal 'python router2.py', in connection of destination node; type to terminal 'python destination.py'

4.) in source type seperated comma sensor list (which must be integer) and then press enter (one example input: 1,2,3,4,5)

5.) then you can see the datas which you sent in destination node with initial order, the statistical things (average end to end delay and etc.) are in comments and they wont be seen as output. If you want to see them you can take them out of the comment in destination.py. If you want to see statistical things, please dont sent one length input (e.g. 1) from source.py.

Experiment 2:

It is unnecessary to repeat 1. and 2. step, because we did them in experiment 1.
3.) in broker, router1, router2 and destination's (source not included) ssh connection, type terminal 'sudo tc qdisc change dev eth0 root netem delay 20ms 5ms', 'sudo tc qdisc change dev eth1 root netem delay 20ms 5ms', 'sudo tc qdisc change dev eth2 root netem delay 20ms 5ms' and also for only broker type 'sudo tc qdisc change dev eth3 root netem delay 20ms 5ms'
3.) in connection of source node; type to terminal 'python source.py' in python, in connection of broker node; type to terminal 'python broker.py', in connection of router1 node; type to terminal 'python router1.py', in connection of router2 node; type to terminal 'python router2.py', in connection of destination node; type to terminal 'python destination.py'
4.) type seperated comma sensor list (which must be integer) and then press enter (one example input: 1,2,3,4,5)
5.) then you can see the datas which you sent in destination node with initial order, the statistical things (average end to end delay and etc.) are in comments and they wont be seen as output. If you want to see them you can take them out of the comment in destination.py.  If you want to see statistical things, please dont sent one length input (e.g. 1) from source.py.

Experiment 3:

It is unnecessary to repeat 1. and 2. step, because we did them in experiment 1.
3.) in broker, router1, router2 and destination's (source not included) ssh connection, type terminal 'sudo tc qdisc change dev eth0 root netem delay 60ms 5ms', 'sudo tc qdisc change dev eth1 root netem delay 60ms 5ms', 'sudo tc qdisc change dev eth2 root netem delay 60ms 5ms' and also for only broker type 'sudo tc qdisc change dev eth3 root netem delay 60ms 5ms'
3.) in connection of source node; type to terminal 'python source.py' in python, in connection of broker node; type to terminal 'python broker.py', in connection of router1 node; type to terminal 'python router1.py', in connection of router2 node; type to terminal 'python router2.py', in connection of destination node; type to terminal 'python destination.py'
4.) type seperated comma sensor list (which must be integer) and then press enter (one example input: 1,2,3,4,5)
5.) then you can see the datas which you sent in destination node with initial order, the statistical things ('average of end-to-end delay' and etc.) are in comments and they wont be seen as output. If you want to see them you can take them out of the comment in destination.py.  If you want to see statistical things, please dont sent one length input (e.g. 1) from source.py.

