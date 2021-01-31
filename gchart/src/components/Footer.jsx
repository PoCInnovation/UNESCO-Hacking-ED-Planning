import React from 'react';
import styled from 'styled-components';

const StyledFooter = styled.div`
	width: 100%;
	height: 8vh;
	
	
	position: fixed;
	bottom: 0;
	background-color: #5299C1;	
	
	text-align: center;
`

const StyledText = styled.div`
	margin-top: 1.5%;
	
	font-size: 20px;
	color: #ffffff;
`

export default function Footer() {
	return (
		<StyledFooter>
			<StyledText>Made by PoC</StyledText>
		</StyledFooter>
	)
}
