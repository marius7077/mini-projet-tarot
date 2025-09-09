<template>
  <div>
    <h2>Télescopes</h2>
    <ul>
      <li v-for="telescope in telescopes" :key="telescope.id">
        {{ telescope.name }} - {{ telescope.center }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Telescopes',
  data() {
    return {
      telescopes: []
    }
  },
  async created() {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/telescopes/')
      this.telescopes = response.data
    } catch (error) {
      console.error('Erreur API :', error)
    }
  }
}
</script>
