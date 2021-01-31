import './App.css';
import Chart from "react-google-charts";
import dotenv from "dotenv";
import data from "./out.json";

dotenv.config();
const regions = [];
Object.keys(data).forEach((key) => {
	const {County, note} = data[key];
	const region = regions.find((e) => e.name === County);
	if (!region) {
		regions.push({
			name: County,
			notes: [note]
		});
	} else {
		region.notes.push(note);
	}
});

regions.forEach((region) => {
	const divider = region.notes.length;
	region.notes = region.notes.reduce((acc, value) => acc + Number(value), 0);
	region.notes = region.notes / divider;
});

console.log(regions);

const formatted_values = [['City', 'Note']];

regions.forEach((region) => {
	const {name, notes} = region;
	const newElem = [name, notes];
	formatted_values.push(newElem);
});

console.log(formatted_values);

function App() {
	return (
		<div>
			<Chart
				width={'1000px'}
				height={'700px'}
				chartType="GeoChart"
				data={formatted_values}
				options={{
					region: 'IE',
					resolution: 'provinces',
					colorAxis: {
						colors: ['#512E5F', '#EBDEF0']
					},
					backgroundColor: '#81d4fa',
					datalessRegionColor: '#ffffff',
					defaultColor: '#85929E',
				}}
				mapsApiKey={process.env.REACT_APP_GCP_API_KEY}
				rootProps={{'data-testid': '2'}}
			/>
			<Chart
				width={'1000px'}
				height={'700px'}
				chartType={"Line"}
				data={[
					['Note', 'Budget (K)'],
					[0, 20],
					[1, 404],
					[2, 192],
					[2, 252],
					[3, 157],
					[4, 1166],
					[5, 325],
					[5, 530],
					[6, 332],
					[8, 1075],
					[9, 2452],
					[10, 2741],
			  ]}
				options={{
					hAxis: {
						title: "My cool h axis"
					},
					vAxis: {
						title: 'My cool v axis',
					},
					chart: {
						title: "Impact of Investments on School Quality",
						subtitle: "in thousand of euros (€)"
					}
				}}
				rootProps={{'data-testid': '1'}}
			/>
		</div>
	)
		;
}

export default App;
