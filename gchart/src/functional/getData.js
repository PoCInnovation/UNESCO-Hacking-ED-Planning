import data from "./../out.json";

// Push JSON data in array
const regions = [];

Object.keys(data).forEach((key) => {
	const {County, note, Roll_No } = data[key];
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

// Average value
regions.forEach((region) => {
	const divider = region.notes.length;
	region.notes = region.notes.reduce((acc, value) => acc + Number(value), 0);
	region.notes = region.notes / divider;
});

// Format value for geographic data
const formattedValues = [['City', 'Note']];
regions.forEach((region) => {
	const {name, notes} = region;
	const newElem = [name, notes];
	formattedValues.push(newElem);
});

export { regions, formattedValues };
