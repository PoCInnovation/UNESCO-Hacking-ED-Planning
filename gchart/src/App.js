import './App.css';
import Chart from "react-google-charts";

// See: https://developers.google.com/chart/interactive/docs/basic_load_libs#load-settings
function App() {
  return (
    <div className="App">
      <Chart
        width={window.innerWidth}
        height={window.innerHeight}
        chartType="GeoChart"
        data={[
          ['City', 'Population', 'Area'],
          ['Dublin', 2761477, 1285.31],
        ]}
        options={{
          backgroundColor: '#D6EAF8',
          region: 'IE',
          displayMode: 'markers',
          resolution: 'provinces',
          colorAxis: { colors: ['green', 'blue'] },
        }}
        mapsApiKey="YOUR_KEY_HERE"
        rootProps={{ 'data-testid': '2' }}
      />
    </div>
  );
}

export default App;
