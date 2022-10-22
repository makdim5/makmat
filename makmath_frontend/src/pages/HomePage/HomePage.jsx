import React from 'react';
import cl from "./HomePage.module.css"
import {AppBar, Button, Toolbar, Typography} from "@mui/material";
import { Link as RouterLink } from "react-router-dom";


const HomePage = () => {
    const headersData = [
        {
            label: "Enter",
            href: "/",
        },

        // {
        //     label: "Log Out",
        //     href: "/logout",
        // },
    ];

    const getMenuButtons = () => {
        return headersData.map(({ label, href }) => {
            return (
                <Button
                    {...{
                        key: label,
                        color: "inherit",
                        to: href,
                        component: RouterLink,

                    }}
                >
                    {label}
                </Button>
            );
        });
    };

    return (
        <div className={cl.home_body}>
            <AppBar >
                <Toolbar>
                    <Typography variant="h6" component="h1">
                        MakMath 2.0
                        {getMenuButtons()}
                    </Typography>
                </Toolbar>
            </AppBar>

            <div style={{backgroundColor:"white"}}>
                Главная
            </div>
        </div>
    );
};

export default HomePage;