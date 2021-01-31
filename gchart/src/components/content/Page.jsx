import React from 'react';
import {makeStyles, useTheme} from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';

import MobileStepper from '@material-ui/core/MobileStepper';
import Button from '@material-ui/core/Button';
import KeyboardArrowLeft from '@material-ui/icons/KeyboardArrowLeft';
import KeyboardArrowRight from '@material-ui/icons/KeyboardArrowRight';

import styled from 'styled-components';

import Map from './Map'
import Table from './Table';
import Stepper from './Stepper';

const useStyles = makeStyles((theme) => ({
	root: {
		padding: "20px"
	},
	rootStepper: {
		maxWidth: 400,
		flexGrow: 1,
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
	const theme = useTheme();
	const types = ['City', 'General', 'Leadership', 'School', 'Pupils', 'Teaching'];
	const [activeStep, setActiveStep] = React.useState(0);

	const handleNext = () => {
		setActiveStep((prevActiveStep) => prevActiveStep + 1);
	};

	const handleBack = () => {
		setActiveStep((prevActiveStep) => prevActiveStep - 1);
	};

	return (
		<StyledPage>
			<Typography align="center" color="secondary" component={"h4"} variant={"h4"}>{types[activeStep + 1]} Notes in Ireland</Typography>
			<Grid container spacing={1} justify="center" className={classes.root} direction="row">
				<Grid item xs={5}>
					<Map name={types[activeStep + 1]} index={activeStep + 1}/>
				</Grid>
				<Grid item xs={3}>
					<Table name={types[activeStep + 1]}/>
				</Grid>
			</Grid>

			<StyledPosition>
				<MobileStepper
					variant="dots"
					steps={5}
					position="static"
					activeStep={activeStep}
					className={classes.rootStepper}
					nextButton={
						<Button size="small" onClick={handleNext} disabled={activeStep === 4}>
							Next
							{theme.direction === 'rtl' ? <KeyboardArrowLeft /> : <KeyboardArrowRight />}
						</Button>
					}
					backButton={
						<Button size="small" onClick={handleBack} disabled={activeStep === 0}>
							{theme.direction === 'rtl' ? <KeyboardArrowRight /> : <KeyboardArrowLeft />}
							Back
						</Button>
					}
				/>
			</StyledPosition>
		</StyledPage>
	)
}
