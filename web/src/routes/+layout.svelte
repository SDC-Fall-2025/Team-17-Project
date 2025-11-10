<script lang="ts">
  import favicon from '$lib/assets/favicon.svg';

  let { children } = $props();

  import '../app.css';
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
</svelte:head>

{@render children?.()}

<hr class="my-2" />
<footer class="my-2">
  <p class="text-center text-sm italic text-gray-500 m-auto w-full">
    This site is run by <a href="https://rapidcow.github.io/site-wisc-sdc-fa25-team/"
      >SDC Fall 2025 Team 17</a
    >. Please review the
    <a href="https://team.endfindme.com/wisc/sdc/fa-25/public/privacy-policy">Privacy Policy</a>
    before using this service.
  </p>
</footer>
