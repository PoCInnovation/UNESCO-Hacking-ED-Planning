import React from 'react';
import styled from 'styled-components';

const StyledHeader = styled.div`
	width: 100%;
	height: 10vh;
	
	background-color: #5299C1;

	text-align: center;
`

const StyledText = styled.div`
	padding-top: 2%;
	
	font-size: 20px;
	color: #ffffff;
`

const StyledImg = styled.img`
	width: 90px;
	height: 70px;
	padding-top: 10px;
`

export default function Header() {
	return (
		<StyledHeader>
			<StyledImg src={"unesco-logo.png"} alt={"unesco logo"}/>
		</StyledHeader>
	)
}
