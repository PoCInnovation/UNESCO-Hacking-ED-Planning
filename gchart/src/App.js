import './App.css';
import Chart from "react-google-charts";
import dotenv from "dotenv";
import data from "./out.json";

dotenv.config();
const regions = [];
Object.keys(data).forEach((key) => {
  const { County, note } = data[key];
  const region = regions.find((e) => e.name === County)
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
  const divider = region.notes.length
  region.notes = region.notes.reduce((acc, value) => acc + Number(value), 0)
  region.notes = region.notes / divider;
});

console.log(regions);

const formatted_values = [['City', 'Note']];

regions.forEach((region) => {
  const {name, notes} = region;
  const newElem = [name, notes];
  formatted_values.push(newElem);
});

console.log(formatted_values)
function App() {
  return (
    <Chart
      width={'1000px'}
      height={'700px'}
      chartType="GeoChart"
      data={formatted_values}
      options={{
        region: 'IE',
        resolution: 'provinces',
        colorAxis: {
          colors: ['#512E5F', '#EBDEF0']},
          backgroundColor: '#81d4fa',
          datalessRegionColor: '#ffffff',
          defaultColor: '#85929E',
      }}
      mapsApiKey={process.env.REACT_APP_GCP_API_KEY}
      rootProps={{ 'data-testid': '2' }}
    />
  );
}

export default App;
