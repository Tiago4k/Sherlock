import React from 'react';
import { useAuth0 } from '../../react-auth0-spa';
// import { Link } from 'react-router-dom';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
    height: 50
  },
  menuButton: {
    marginRight: theme.spacing(2)
  },
  title: {
    flexGrow: 1
  }
}));

const ButtonAppBar = () => {
  const classes = useStyles();
  const { isAuthenticated, loginWithRedirect, logout } = useAuth0();

  return (
    <div className={classes.root}>
      <AppBar position='fixed' style={{ background: '#333333' }}>
        <Toolbar>
          <IconButton
            edge='start'
            className={classes.menuButton}
            color='inherit'
            aria-label='menu'
          >
            <MenuIcon />
          </IconButton>
          <Typography variant='h5' className={classes.title}>
            Sherlock
          </Typography>
          {!isAuthenticated && (
            <Button color='inherit' onClick={() => loginWithRedirect({})}>
              Log in
            </Button>
          )}
          {isAuthenticated && (
            <Button color='inherit' onClick={() => logout()}>
              Log out
            </Button>
          )}
          {/* {isAuthenticated && (
            <span>
              <Link to='/'>Home</Link>&nbsp;
              <Link to='/profile'>Profile</Link>
            </span>
          )} */}
        </Toolbar>
      </AppBar>
    </div>
  );
};

export default ButtonAppBar;
