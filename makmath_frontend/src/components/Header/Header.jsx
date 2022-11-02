import React, {useState} from 'react';
import cl from "./Header.module.css"
import logo from "../../pages/AuthorizationPage/logo.png";
import {NavLink} from "react-router-dom";

const Header = () => {

    const [access, setAccess] = useState(localStorage.getItem('accessToken'))
    return (
        <header className={cl.header}>
            <div className={cl.wrap_logo}>
                <div className={cl.img_block}>
                    <img src={logo} alt="MakMath logo"/>
                </div>
                <NavLink to="/" className={cl.logo}>MakMath 2.0</NavLink>
            </div>
            <nav className={cl.nav}>
                <NavLink className={cl.active} to="#">Главная</NavLink>

                {access !== ""
                    ?
                    < NavLink to="/" onClick={() => { localStorage.setItem('accessToken', ""); window.location.reload() }} >Выйти</NavLink>
                    :
                    <NavLink to="/login">Войти</NavLink>
                }
                <NavLink to="#">О сайте</NavLink>
            </nav>
        </header>
    );
};

export default Header;