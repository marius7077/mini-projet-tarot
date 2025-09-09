<template>
  <div>
    <h2>Centres</h2>
    <ul>
      <li v-for="center in centers" :key="center.id">
        <strong>{{ center.name }}</strong> - {{ center.location }}
        <ul>
          <li v-for="telescope in center.telescopes" :key="telescope.id">
            {{ telescope.name }} ({{ telescope.description }})
          </li>
          <li v-for="employee in center.employees" :key="employee.id">
            {{ employee.first_name }} {{ employee.last_name }} - {{ employee.role }}
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Centers',
  data() {
    return {
      centers: []
    }
  },
  async created() {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/centers/')
      this.centers = response.data
    } catch (error) {
      console.error('Erreur API :', error)
    }
  }
}
</script>
