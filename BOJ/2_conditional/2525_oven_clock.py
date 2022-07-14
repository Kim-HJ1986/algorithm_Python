hh, mm = map(int, input().split())
term = int(input())

term_hour = term // 60
term_minute = term % 60

end_hour = hh + term_hour
end_minute = mm + term_minute

if end_minute > 59:
    end_hour += 1
    end_minute -= 60

if end_hour > 23:
    print(end_hour - 24, end_minute)
else:
    print(end_hour, end_minute)
