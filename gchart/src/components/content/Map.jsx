import Chart from "react-google-charts";
import React from "react";
import styled from 'styled-components';

import { formattedValues } from '../../functional/mergeJson';

const StyledMapContainer = styled.div`
	width: 500px;
	height: 542px;

	margin-top: 25px;
	box-shadow: 5px 5px 10px #cccccc;
`

formattedValues.shift();

export default function Map(props) {
	const res = [['City', props.name]]

	res.push(...formattedValues.map((e) => [e[0], Number(e[props.index])]));
	return (
		<StyledMapContainer>
			<Chart
				width={'500px'}
				height={'542px'}
				chartType="GeoChart"
				data={res}
				options={{
					region: 'IE',
					resolution: 'provinces',
					colorAxis: {
						colors: ['#512E5F', '#EBDEF0']
					},
					backgroundColor: '#81d4fa',
					datalessRegionColor: '#ffffff',
					defaultColor: '#85929E',
					tooltip: {
						boxShadow: "5px 5px 10px #cccccc",
					}
				}}
				mapsApiKey={process.env.REACT_APP_GCP_API_KEY}
				rootProps={{'data-testid': '2'}}
			/>
		</StyledMapContainer>
	);
}

/*<Chart
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
/>*/

