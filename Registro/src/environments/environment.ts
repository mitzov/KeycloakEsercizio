export const environment = {
  production: false,
  keycloak: {
    url: 'URL DI KEYCLOAK SENZA LO / FINALE',
    realm: 'NOME DEL REALM CREATO SU KEYCLOAK',
    clientId: 'CLIENT ID INSERITO SU KEYCKLOAK',
    redirectUri: window.location.origin,
  }
};