import adapter from '@sveltejs/adapter-static';

const config = {
  kit: {
    adapter: adapter({
      pages: 'build',
      assets: 'build',
      fallback: 'index.html', // 👈 important for SPA behavior
      precompress: false
    })
  }
};

export default config;
