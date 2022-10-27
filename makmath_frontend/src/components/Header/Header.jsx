import React from 'react';
import cl from "./Header.module.css"
import logo from "../../pages/AuthorizationPage/logo.png";

const Header = () => {
    return (
        <header className={cl.header}>
            <div className={cl.wrap_logo}>
                <div className={cl.img_block}>
                    <img src={logo} alt="MakMath logo"/>
                </div>
                {/* eslint-disable-next-line jsx-a11y/anchor-is-valid */}
                <a className={cl.logo}>MakMath 2.0</a>
            </div>
            <nav className={cl.nav}>
                {/* eslint-disable-next-line jsx-a11y/anchor-is-valid */}
                <a className={cl.active} href="#">Главная</a>
                {/* eslint-disable-next-line jsx-a11y/anchor-is-valid */}
                <a href="\login">Войти</a>
                {/* eslint-disable-next-line jsx-a11y/anchor-is-valid */}
                <a href="#">О сайте</a>
            </nav>
        </header>
    );
};

export default Header;