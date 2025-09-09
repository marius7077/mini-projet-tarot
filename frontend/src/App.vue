<template>
  <div>
    <h1>Projet TAROT</h1>
    <Centers />
    <Telescopes />
    <Events />
  </div>
</template>

<script>
import Centers from './components/Centers.vue'
import Telescopes from './components/Telescopes.vue'
import Events from './components/Events.vue'

export default {
  components: { Centers, Telescopes, Events }
}
</script>
