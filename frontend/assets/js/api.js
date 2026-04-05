// Centralized API helper for all frontend requests.
const API = (() => {
  const getToken = () => localStorage.getItem('auth_token');

  async function request(endpoint, method = 'GET', body = null, isBlob = false) {
    const headers = { 'Content-Type': 'application/json' };
    const token = getToken();
    if (token) headers.Authorization = `Bearer ${token}`;

    const response = await fetch(`${window.APP_CONFIG.apiBaseUrl}${endpoint}`, {
      method,
      headers,
      body: body ? JSON.stringify(body) : null,
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({ error: 'Unknown API error' }));
      throw new Error(errorData.error || 'Request failed');
    }

    if (isBlob) return response.blob();
    return response.json();
  }

  return {
    login: (payload) => request('/login', 'POST', payload),
    getProducts: (params = '') => request(`/products${params}`),
    createProduct: (payload) => request('/products', 'POST', payload),
    updateProduct: (id, payload) => request(`/products/${id}`, 'PUT', payload),
    deleteProduct: (id) => request(`/products/${id}`, 'DELETE'),
    getTransactions: () => request('/transactions'),
    createTransaction: (payload) => request('/transactions', 'POST', payload),
    getDashboard: () => request('/dashboard'),
    getPrediction: (id) => request(`/predict/${id}`),
    exportReport: () => request('/reports/export', 'GET', null, true),
  };
})();
