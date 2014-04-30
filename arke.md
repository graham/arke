# Arke
###### because it shouldn't be hard.

## Purpose
The purpose of Arke is to make building both servers and clients easy. In the last couple years building real web services has become a largely custom solution every time.

__Arke should change that__

Arke is a ___definition___ as well as a couple ___reference implementations___. The goal of Arke is not to be a end-all-implementation, but rather to be a common language so that APIs can tie servers and clients together more easily.

## What Arke is not
Arke will likely not be the thing that your system runs on if you grow to be the size of Dropbox or Twitter (it may), it will hopefully make your development early on considerably easier.

## What Arke is
Arke should make your development easier, you should be able to spool up new clients easily, and replace old server architecture without anyone knowing.

# On to the spec.

`/_api_list` = Every implementation will represent the endpoints it presents via this command. This can be filtered and abbreviated (as well as cached) in order to keep the bandwidth down, but clients can reliably hit this endpoint on any Arke service.

`/_version` = A more lightweight way for clients to make sure they have the current version, this isn't required, but some clients may reason via it so if you end up implementing it you should make sure it works correctly.

## Clients
Client should generally expose functionality in one of two ways, either as a proxy object:

In Python: `/user/create?id=1` becomes `client.user.create(id=1)`

Or Javascript: `/user/create?id=1` becomes `client.user.create({'id':1})`

And Erlang: `/user/create?id=1` becomes `client:call(Info, "user.create", [{id, 1}])`

Alternatively clients will provide `_call()` which allows clients to invoke functions without building proxy objects (much better for some types of languages).

Clients should also include `_has_call()` so that applications can introspect into what functions are available.

## Implementations

To start Arke will implement the following server and client implementations.

Server:

  - Python
  - Javascript (NodeJS)
  - Erlang
  - Go

Client:  

  - Python
  - Javascript (browser / NodeJS)
  - Erlang
  - Objective C
  - C

Layers:

  - HTTP (most common)
  - Unix File Socket
  - ZeroMQ
  - RabbitMQ
  - Redis Queue

## Thoughts about API development

I consistently hear about projects that don't get off the ground because some of the small details around how they communicate end up getting all of the focus. 