name = raw_input('Please enter your name:')
job = raw_input('job:')
salary = raw_input('salary:')

real_age = 29

# print type(age)
for i in range(10):
    age = input('age:')
    if age > 29:
        print 'Think smaller!'
    elif age == 29:
        print 'Bingo!'
        break
    else:
        print 'Think bigger!.'
    print 'You still got %s shots!' % (9 - i)

print '''
Personal information of %s:
          Name: %s
          Age : %d
          Job : %s
        Salary: %s
--------------------------

''' %(name, name, age, job, salary)