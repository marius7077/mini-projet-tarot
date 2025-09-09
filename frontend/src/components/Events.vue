<template>
  <div>
    <h2>Événements</h2>
    <ul>
      <li v-for="event in events" :key="event.id">
        {{ event.name }} ({{ event.event_type }}) observé par {{ event.telescope.name }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Events',
  data() {
    return {
      events: []
    }
  },
  async created() {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/events/')
      this.events = response.data
    } catch (error) {
      console.error('Erreur API :', error)
    }
  }
}
</script>
