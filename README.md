# reductor influxdb agent

simple influxdb client + daemon + metric collector for carbon reductor (https://twitter.com/carbon_reductor)

curl / python / bash

## metrics

- url count in kernel module
- activation state
- http url counter (before load to kernel)
- size of ipset with https resources
- config length (if 0 - you have very bad time)
- rx bytes/packets/errors/dropped of every interface in bridge (mirror) 
