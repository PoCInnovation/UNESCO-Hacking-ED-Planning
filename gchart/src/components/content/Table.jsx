import React from 'react';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';

import makeStyles from "@material-ui/core/styles/makeStyles";
import TableCell from "@material-ui/core/TableCell";
import { regions as rows } from '../../functional/getData'

const useStyles = makeStyles({
	container: {
		maxHeight: 600,
		minWidth: 300,
		maxWidth: 300,

		boxShadow: "5px 5px 10px #cccccc",
	},
});

export default function MyTable(props) {
	const classes = useStyles();

	return (
			<TableContainer className={classes.container} >
				<Table stickyHeader>
					<TableHead>
						<TableRow>
							<TableCell>Régions</TableCell>
							<TableCell align="right">Notes</TableCell>
						</TableRow>
					</TableHead>
					<TableBody>
						{rows.map((row) => (
							<TableRow key={row.name}>
								<TableCell scope={"row"}>
									{row.name}
								</TableCell>
								<TableCell align="right">{(row.notes).toFixed(2)}</TableCell>
							</TableRow>
						))}
					</TableBody>
				</Table>
			</TableContainer>
	)
}
