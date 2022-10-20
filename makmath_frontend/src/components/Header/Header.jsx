import React from "react";

import {
    AppBar,
    Toolbar,
    IconButton,
    Button, Typography
} from "@mui/material";

import MenuIcon from '@mui/icons-material/Menu';

const navigationLinks = [
    {name: "About", href: ""},
    {name: "Projects", href: ""},
    {name: "Resume", href: ""},
];


export default function Header() {

    return (
        <AppBar position="static">
            <Toolbar>
                <IconButton
                    size="large"
                    edge="start"
                    color="inherit"
                    aria-label="menu"
                    sx={{mr: 2}}
                >
                    <MenuIcon/>
                </IconButton>
                <Typography variant="h6" component="div" sx={{flexGrow: 1}}>
                    MakMath 2
                </Typography>

            </Toolbar>
        </AppBar>
    );
}