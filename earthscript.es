include time

func sayHello(name)[
    balls = name
    print(f'Hello, <balls>')
    time.sleep(1)
    print(f'Goodbye, <balls>')
];

// runs the main function
sayHello('Adam');