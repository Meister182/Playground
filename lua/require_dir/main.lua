#! /usr/bin/env lua
require("foo")

-- Can't find bar.lua
-- require("bar")

-- Works but, won't be required a second time
require("foo.bar")

-- dofile will "reload" the file everytime
print("dofile loading:")
dofile("foo/bar.lua")
dofile("foo/bar.lua")
dofile("foo/bar.lua")
dofile("foo/bar.lua")
