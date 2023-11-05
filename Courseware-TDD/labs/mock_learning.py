from unittest.mock import Mock

foo = Mock()
foo.bar.return_value = 0

print(type(foo))
print(type(foo.bar))
print(type(foo.bar.return_value))

print(foo)
print(foo.bar)

print(dir(foo))
print("bar" in dir(foo))

foo.baz
foo.baz.return_value = 1
print(dir(foo))
print("baz" in dir(foo))

print(foo.return_value)
# help(dir)

print(foo.called)
x = foo("Once")
print(foo.called)
print(foo.call_args)

x = foo("Twice")
print(foo.called)
print(foo.call_args)

print(foo.call_args_list)
print(foo.call_count)

foo.Mock()
print(foo.called)
x = foo("Once")
print(foo.called)
print(foo.call_args)

x = foo("Twice")
print(foo.called)
print(foo.call_args)

foo.assert_called_once()
