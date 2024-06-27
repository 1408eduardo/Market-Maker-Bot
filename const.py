const { ethers } = require("ethers");
const UNISWAP = require("@uniswap/sdk");
const fs = require('fs');
const { Token, WETH, Fetcher, Route, Trade, TokenAmount, TradeType, Percent } = require("@uniswap/sdk");
const okxBridgeApi = require('okx-bridge-api');

// Configuración de la red y el proveedor
const provider = new ethers.providers.JsonRpcProvider('https://bsc-dataseed.binance.org/');

// Direcciones de los contratos de tokens
const USDC_SEPOLIA_ADDRESS = '0x...'; // Dirección del contrato USDC Sepolia
const ETHEREUM_ADDRESS = '0x...'; // Dirección del contrato Ethereum

// Crear instancias de los tokens
const USDC_SEPOLIA = new Token(UNISWAP.ChainId.MAINNET, USDC_SEPOLIA_ADDRESS, 18);
const ETHEREUM = new Token(UNISWAP.ChainId.MAINNET, ETHEREUM_ADDRESS, 18);

// Configuración de la API de OKX
const okxApi = new okxBridgeApi({
  apiKey: '33bfe871-b6a5-4391-aeeb-cca4ce971548',
  apiSecret: '0F1A96741B083277007AA84F61A716C5'
});

// Función para cambiar tokens
async function swapTokens(tokenIn, tokenOut, amount) {
  // Obtener la ruta óptima para el cambio de tokens
  const route = await getOptimalRoute(tokenIn, tokenOut, amount);

  // Realizar el cambio de tokens
  const trade = new Trade(route, new TokenAmount(tokenIn, amount), TradeType.EXACT_IN);
  const txData = await okxApi.buildTx(trade);
  await provider.sendTransaction(txData);
}

// Función para obtener la ruta óptima para el cambio de tokens
async function getOptimalRoute(tokenIn, tokenOut, amount) {
  // Obtener la lista de pares de tokens soportados por OKX
  const supportedPairs = await okxApi.getSupportedPairs();

  // Filtrar los pares que incluyen el token de entrada y salida
  const filteredPairs = supportedPairs.filter(pair => pair.tokenIn === tokenIn.address && pair.tokenOut === tokenOut.address);

  // Obtener la ruta óptima basada en la lista de pares filtrados
  const optimalRoute = await okxApi.getOptimalRoute(filteredPairs, amount);

  return optimalRoute;
}

// Ejecutar la función de cambio de tokens
swapTokens(USDC_SEPOLIA, ETHEREUM, '200000');
