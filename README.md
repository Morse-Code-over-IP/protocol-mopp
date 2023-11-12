
# Morse Code Over Packet Protocol (MOPP) - UDP

## Introduction

MOPP is a protocol designed for the transmission of Morse code over data protocols that use payloads consisting of 8-bit bytes. It is suitable for both LoRa and IP networks, where byte strings are transmitted as packet payloads.

This protocol description outlines the structure of MOPP packets, the encoding of Morse code elements, and how the protocol can be used over UDP for IP networks.

The current document describes version 1 of the protocol.

## Design Goals

- Allow faithful transmission of Morse code.
- Support multiple languages and characters.
- Include information about the original speed.
- Be efficient to accommodate bandwidth constraints.
- Avoid the use of Zero bytes to prevent misinterpretation.
- Use UDP as the transport layer for IP networks.

## Protocol Structure

### Packet Structure:

- 2 bits: Protocol Version (01b for version 1)
- 6 bits: Serial Number
- 6 bits: Speed at origin in WpM (Words per Minute, 5 - 60 decimal)

### Payload:

The payload consists of Morse code information encoded as follows:

- 2 bits for each Morse code element:
  - 01b: dit
  - 10b: dah
  - 00b: End of Character (EOC)
  - 11b: End of Word (EOW)


#### Heartbeat (Modification for UDP Chat Server)

The MOPP UDP Chat server is always trying to receive packets. If nothing is sent, the connection will timeout.
This timeout triggers the sending of empty hearbeat packets to all clients (no payload).
If the clients respond, their session gets updated.


### Complete Packet Format:

```
+----------------------+-------------------+
| Protocol Version     | Serial Number     |
+----------------------+-------------------+
| Speed at Origin (WpM)| Payload           |
+----------------------+-------------------+
```

## Example:

Let's consider the Morse code for the word "PARIS" at a speed of 16 WpM:

- Protocol Version: 01
- Serial Number: 011011
- Speed: 010000
- 'P' (di dah dah dit EOC): 01 10 10 01 00
- 'A' (di dah EOC): 01 10 00
- 'R' (di dah dit EOC): 01 10 01 00
- 'I' (di dit EOC): 01 01 00
- 'S' (di di dit EOW): 01 01 01 11

Packing into a byte string:

`01011011 01000001 10100100 01100001 10010001 01000101 01110000`

In hexadecimal notation:

`5B 41 A4 61 91 45 70`

As an ASCII string:

```
[A¤a`Ep
```

## UDP Transmission:

- Use UDP for packet transmission.
- Send the MOPP packet as the payload of the UDP packet.
- Define a port for MOPP communication (standard 7373).

## Conclusion

MOPP over UDP provides an efficient and language-agnostic method for transmitting Morse code over IP networks, 
catering to the constraints of bandwidth and ensuring faithful representation of Morse code messages.

# References
- [Original MOPP Protocol description](https://github.com/oe1wkl/Morserino-32/blob/master/Documentation/Protocol%20Description/morse_code_over_packet_protocol.md) ([Local copy](./doc/protocol-mopp.orig.md)) by Willi, OE1WKL
- Encoder and Decoder in Python: implementation taken from [Sigbit](https://github.com/tuxintrouble/sigbit) by Sebastian Stetter, DJ5SE
