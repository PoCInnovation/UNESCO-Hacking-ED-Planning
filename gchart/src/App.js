import React from "react";
import 'fontsource-roboto';
import './App.css';
import Chart from "react-google-charts";

import dotenv from "dotenv";

import Header from './components/Header';
import Footer from './components/Footer';
import Page from './components/content/Page';

import { regions } from './functional/mergeJson';

import {createMuiTheme, ThemeProvider} from '@material-ui/core/styles';
import purple from '@material-ui/core/colors/purple';
import green from '@material-ui/core/colors/green';



dotenv.config();



const theme = createMuiTheme({
	palette: {
		primary: {
			main: "#ffffff",
		},
		secondary: {
			main: "#5299C1",
		},
	},
});


function App() {
	return (
		<div>
			<ThemeProvider theme={theme}>
				<Header/>
				<Page/>
				<Footer/>
			</ThemeProvider>
		</div>

	);
}

export default App;
