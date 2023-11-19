###
#
#  It sorts integer arguments (ascending)
#
###

result = []
ARGV.each do |arg|
    # jump if not integer
    next if arg !~ /^-?[0-9]+$/

    # change to integer
    i_arg = arg.to_i

    # adds result at right position
    is_inserted = false
    x = 0
    r = result.size
    while !is_inserted && x < r do
        if result[x] < i_arg
            x += 1
        else
            result.insert(x, i_arg)
            is_inserted = true
            break
        end
    end
    result << i_arg if !is_inserted
end

puts result
