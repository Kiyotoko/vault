def josephus_permutation(n, k)
    l = (1..n).to_a
    r = []
    i = 0
    while l.length > 0
        i += 1
        if i < k
            l.push(l[0])
        else
            r.push(l[0])
            i = 0
        end
        l.shift
    end
    return r
end

def josephus_last(n, k)
    if n == 1
        return 1
    end
    return ((josephus_last(n - 1, k) + k - 1) % n) + 1
end

for i in 1..10 do
    p josephus_permutation(i, 2)
end

puts josephus_last(19, 4)