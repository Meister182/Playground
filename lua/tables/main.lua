#! /usr/bin/env lua
function tprint (tbl, indent)
  if not indent then indent = 0 end
  local toprint = string.rep(" ", indent) .. "{\r\n"
  indent = indent + 2 
  for k, v in pairs(tbl) do
    toprint = toprint .. string.rep(" ", indent)
    if (type(k) == "number") then
      toprint = toprint .. "[" .. k .. "] = "
    elseif (type(k) == "string") then
      toprint = toprint  .. k ..  "= "   
    end
    if (type(v) == "number") then
      toprint = toprint .. v .. ",\r\n"
    elseif (type(v) == "string") then
      toprint = toprint .. "\"" .. v .. "\",\r\n"
    elseif (type(v) == "table") then
      toprint = toprint .. tprint(v, indent + 2) .. ",\r\n"
    else
      toprint = toprint .. "\"" .. tostring(v) .. "\",\r\n"
    end
  end
  toprint = toprint .. string.rep(" ", indent-2) .. "}"
  return toprint
end

-- Creating table
t = {1,2,3}

t = {
    1,
    3,
    test = "dummy",
    config = {
        option_1 = "ON",
        option_2 = "OFF"
    }
--    print("Does this print?") NO!
}

-- print the table
print(string.rep('-', 30))
print(tprint(t))

-- accesing the table content
print(string.rep('-', 30))
print("index: " .. t[2])
print("key: " .. t["test"])
print("property: " .. tprint(t.config))
