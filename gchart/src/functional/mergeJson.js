import NLPdata from '../data.json';
import local from '../out.json';

// Push JSON data in array
const regions = [];
const data = [];

Object.keys(local).forEach((key) => {
	const {County, note, Roll_No } = local[key];
	const region = regions.find((e) => e.name === County);
	if (!region) {
		regions.push({
			name: County,
			roll: Roll_No,
			notes: [note]
		});
	} else {
		region.notes.push(note);
	}
});


let count = 0;

Object.keys(NLPdata).forEach((key) => {
	const { Roll_No, data } = NLPdata[key];

	const school = regions.find((e) => {
		if (Roll_No !== "NaN") {
			console.log(e.roll, Roll_No);
		}
		return e.roll === Roll_No
	})
	if (school) {
		console.log(school.roll, Roll_No);
	} else {
		count += 1;
	}
});

console.log(count);
// {name: "Carlow", roll: "00651R", notes: Array(42)}

export { regions }
