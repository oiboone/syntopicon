function RawInline(elem)
    x = elem.c[2]
    if not (x == nil) then
        i=string.find (x, "&#8853;")
        if not (i == nil) then
            elem.c[2]=string.sub (x,1,i-1).."<sup>&#8224;</sup>"..string.sub(x,i+7)
        end
    end
    
    return elem
end

--  strfind (str, substr, [init, [end]])