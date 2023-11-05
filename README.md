# Protocol MOPP Description and Libraries

Libaries (WIP) for python and javascript are provided in this repository.

# Heartbeat (UDP Chat Server)
Explanation: we are always trying to receive packets. If nothing is sent, the connection will timeout.
This timeout triggers the sending of empty hearbeat packets to all clients. If the clients respond, their session gets updated.

# References
- [Original MOPP Protocol description](https://github.com/oe1wkl/Morserino-32/blob/master/Documentation/Protocol%20Description/morse_code_over_packet_protocol.md)
- [Local copy of the protocol description](./protocol-mopp.md)
