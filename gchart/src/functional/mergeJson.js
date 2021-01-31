import NLPdata from '../data.json';
import local from '../out.json';

// Push JSON data in array
const regions = [];
const data = [];

function getRandomInt(max) {
	return Math.floor(Math.random() * Math.floor(max));
}

Object.keys(local).forEach((key) => {
	const {County, Roll_No } = local[key];
	const region = regions.find((e) => e.name === County);
	if (!region) {
		regions.push({
			name: County,
			categories: ["General", "Pupils", "Teaching", "Support", "Leadership", "School"],
			rolls: [Roll_No],
			General: [getRandomInt(100)],
			Teaching: [getRandomInt(100)],
			Pupils: [getRandomInt(100)],
			Support: [getRandomInt(100)],
			Leadership: [getRandomInt(100)],
			School: [getRandomInt(100)]
		});
	} else {
		region.rolls.push(Roll_No);
		region.General.push(getRandomInt(100));
		region.Teaching.push(getRandomInt(100));
		region.Pupils.push(getRandomInt(100));
		region.Support.push(getRandomInt(100));
		region.Leadership.push(getRandomInt(100));
		region.School.push(getRandomInt(100));
	}
});



Object.keys(NLPdata).forEach((key) => {
	const { Roll_No, note, data } = NLPdata[key];
	const { pupils, teaching, support, leadership, school } = data;

	const tmpSchool = regions.find((e) => {
		const roll = e.rolls.find((x) => x === Roll_No);
		return roll !== undefined;
	});
	if (tmpSchool) {
		tmpSchool.General.push(note * 100);
		tmpSchool.Pupils.push(pupils * 100);
		tmpSchool.Teaching.push(teaching * 100);
		tmpSchool.Support.push(support * 100);
		tmpSchool.Leadership.push(leadership * 100);
		tmpSchool.School.push(school * 100);
	}
});

// Average value
regions.forEach((region) => {
	const GeneralDivider = region.General.length;
	region.General = region.General.reduce((acc, value) => acc + Number(value), 0);
	region.General = (region.General / GeneralDivider).toFixed(2);

	const PupilsDivider = region.Pupils.length;
	region.Pupils = region.Pupils.reduce((acc, value) => acc + Number(value), 0);
	region.Pupils = (region.Pupils / PupilsDivider).toFixed(2);

	const TeachingDivider = region.Teaching.length;
	region.Teaching = region.Teaching.reduce((acc, value) => acc + Number(value), 0);
	region.Teaching = (region.Teaching / TeachingDivider).toFixed(2);

	const LeadershipDivider = region.Leadership.length;
	region.Leadership = region.Leadership.reduce((acc, value) => acc + Number(value), 0);
	region.Leadership = (region.Leadership / LeadershipDivider).toFixed(2);

	const SchoolDivider = region.School.length;
	region.School = region.School.reduce((acc, value) => acc + Number(value), 0);
	region.School = (region.School / SchoolDivider).toFixed(2);
});


// Format value for geographic data
const formattedValues = [['City', 'General', 'Leadership', 'School', 'Pupils', 'Teaching']];
regions.forEach((region) => {
	const {name, General, Leadership, School, Pupils, Teaching} = region;
	const newElem = [name, General, Leadership, School, Pupils, Teaching];

	formattedValues.push(newElem);
});

// {name: "Carlow", roll: "00651R", notes: Array(42)}

export { regions, formattedValues };
