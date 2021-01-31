import React from 'react';
import { makeStyles } from '@material-ui/core/styles'
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';

import styled from 'styled-components';

import Map from './Map'
import Table from './Table';
import Stepper from './Stepper';

const useStyles = makeStyles((theme) => ({
	root: {
		padding: "20px"
	},
}));

const StyledPage = styled.div`
	width: 98.9vw;
	height: 84vh;
	
	margin: 0;
	padding: 10px;
	background-color: #ffffff;
	text-align: center;

`

const StyledPosition = styled.div`	
	margin-top: 40px;
	padding-left: 40%;
	position: center;
`

export default function Page()
{
	const classes = useStyles();
	return (
		<StyledPage>
			<Typography align="center" color="secondary" component={"h4"} variant={"h4"}>Title of my visu</Typography>
			<Grid container spacing={1} justify="center" className={classes.root} direction="row">
				<Grid item xs={5}>
					<Map/>
				</Grid>
				<Grid item xs={3}>
					<Table/>
				</Grid>
			</Grid>

			<StyledPosition>
				<Stepper/>
			</StyledPosition>
		</StyledPage>
	)
}
