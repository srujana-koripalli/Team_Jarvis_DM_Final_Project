import React, { useState } from 'react';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import axios from 'axios'

const theme = createTheme();

export default function TestModel () {
  const [zipcode, setZipcode] = React.useState('')
  const [zestimate, setZestimate] = React.useState('')
  const [rent_zestimate, setRentZestimate] = React.useState('')
  const [price, setPrice] = React.useState('')
  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    // eslint-disable-next-line no-console
  };

  const handleClick = async() => {
    var url = "http://127.0.0.1:5000/predictInvestment/" + price + "/" + zestimate + "/" + rent_zestimate + "/" + zipcode
    console.log(url)
    await fetch(url)
      .then(function (response) {
        alert(response)
      })
      .catch(function (error) {
        console.log(error)
        // reject(error);
      });
  }
  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Typography component="h1" variant="h5">
            Prediction
          </Typography>
          <Box component="form" noValidate sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="zipcode"
              label="Zip Code"
              name="zipcode"
              autoComplete="zipcode"
              onChange = {(event) => setZipcode(event.target.value)}
              autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="zestimate"
              label="zestimate"
              id="zestimate"
              onChange={(event) => setZestimate(event.target.value)}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="rentZestimate"
              label="Rent Zestimate"
              id="rentzestimate"
              onChange={(event) => setRentZestimate(event.target.value)}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="price"
              label="Listed Price"
              id="price"
              onChange={(event) => setPrice(event.target.value)}
            />
           
            <Button
              // type="submit"
              fullWidth
              onClick={() => handleClick()}
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Evaluate
            </Button>
            <Grid container>
            </Grid>
          </Box>
        </Box>
      
      </Container>
    </ThemeProvider>
  );
}