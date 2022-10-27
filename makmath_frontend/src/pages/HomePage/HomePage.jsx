import React from 'react';
import cl from "./HomePage.module.css"
import {AppBar, Button, Toolbar, Typography} from "@mui/material";
import { Link as RouterLink } from "react-router-dom";
import Header from "../../components/Header/Header";
import FeatureScene from "../../components/FeatureScene/FeatureScene";


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

            <Header></Header>

            <div style={{height:1500}}></div>

            <div className={cl.features}>
                <FeatureScene></FeatureScene>

                <FeatureScene></FeatureScene>

                <FeatureScene></FeatureScene>

                <FeatureScene></FeatureScene>
            </div>


        </div>
    );
};

export default HomePage;