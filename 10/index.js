

const scheduler = (f, n) => {
	// Call f after n milliseconds
	setTimeout(f, n);
}


const test = () => { console.log("Hello world!") }

scheduler(test, 1000);
