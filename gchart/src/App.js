import './App.css';
import Chart from "react-google-charts";
import dotenv from "dotenv";
import data from "./out.json";

dotenv.config();

const regions = []

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

// See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
function App() {
  return (
    /*
    <Chart
      width={'1000px'}
      height={'700px'}
      chartType="GeoChart"
      data={[
        ['City', 'School Name', 'Note'],
        ['Carlow', 'BALLYCONNELL N S', 4],
        ['Carlow', 'BORRIS MXD N S', 9],
        ['Clare', 'S N MHUIRE MILIUC', 3],
      ]}
      options={{
        region: 'IE',
        displayMode: 'markers',
        resolution: 'provinces',
        colorAxis: { colors: ['green', 'blue'] },
      }}
      mapsApiKey={process.env.REACT_APP_GCP_API_KEY}
      rootProps={{ 'data-testid': '2' }}
    />
    */
   <div>
     PtitLuca
   </div>
  );
}

export default App;
