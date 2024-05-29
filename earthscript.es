include time

func sayHello(name)[
    balls = name
    print(f'Hello, <name>')
    time.sleep(1)
    print(f'Goodbye, <name>')
];

// runs the main function
sayHello('Person');
