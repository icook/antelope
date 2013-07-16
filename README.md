Antelope
========

Antelope is (will be) a simple, lightweight finance tracking system. It's
overall goals are:

+ Track credits and debits for each month, with the goal of a
  balanced book. If it gained or lost you money there should be a proper way to
  record it.
+ Allow any arbitrary identifier to accompany a transaction. Datastore will be
  backed by mongodb, so adding attributes should be seamless. These attributes
  will then be used to drive reports, such as where you spent money.
+ A pluggable import system, allowing import of bulk data from other sources.
+ Decentralized. I don't currenlty have any desire to worry about the security
  features that a production version of this software would require, therefore
  if it becomes popular it will be somehting you setup on your own machine. At
  least for a while.

Tech Stack
==========

Antelope is currently using the follwing technolgies:

1. Flask Python microframework
2. Yota Python form library
3. MongoDB data store

Future plans:
+ Data visualization with D3

License
=======

This software is freely availible under the MIT license.
