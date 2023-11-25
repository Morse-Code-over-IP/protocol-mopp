
# JSON Payload Documentation

## Outline

+ version: protocol version
+ sender: optional string with name of sender
+ receiver: optional string with name of receiver
+ at least one of the three 
  1. raw_payload_mopp: optional mopp encoded binary data
  2. raw_payload_cwcom: optional cwcom encoded binary data
  3. durations: optional int-array with durations of the individual morse signals
+ wpm: optional integer with words-per-minute
+ relayed: optional string with name of the server, where this packes has been relayed from
+ channel: optional string with name of the channel / frequency / wire

## Version 1

The payload for version 1 has the following structure:

```json
{
  "version": 1,
  "durations": [60, -60, 180, -60, 380, -60],
}
```

## Versions later

```json
{
  "version": 2,
    "raw_payload_mopp": "Base64 of encoded raw MOPP data",

  "sender": "Optional string with name of the sender",
  "receiver": "Optional string with name of the receiver",
  "raw_payload_mopp": "Base64 of encoded raw MOPP data",
  "raw_payload_cwcom": "Base64 of encoded raw CWCom data",
  "durations": [60, -60, 180, -60, 380, -60],
}
```



# WIP Channels


moip/channel/name
             mopp/
moip/channel/name
             cwcom/

moip/channel/name
             durations/

moip/listchannels

"durations": [60, -60, 180, -60, 180, -60]
... WIP

mosquitto_pub -h broker.hivemq.com -t  /moip/udp2mqtt/durations -m '{ "durations": [60, -60, 180, -60, 380, -60], "version": 1 }'




channel = mtc.kob..._wire1
channel = udp_mopp.... 

