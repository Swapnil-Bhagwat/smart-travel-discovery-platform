import assert from "node:assert";

const FRONTEND_URL = "http://localhost:3000";
const BACKEND_URL = "http://localhost:5000/api/v1";

async function verifySearchFlowUX() {
  console.log("=== Verifying Search Flow UX Updates ===");

  // 1. Fetch homepage and verify DOM structure
  const homeRes = await fetch(`${FRONTEND_URL}/`);
  assert.strictEqual(homeRes.status, 200, "Homepage must return 200 OK");
  const homeHtml = await homeRes.text();

  // Assert single action button
  assert.ok(homeHtml.includes("Search Packages"), "Must have 'Search Packages' button");
  assert.ok(!homeHtml.includes("Discover Destinations</button>"), "Must NOT have 'Discover Destinations' button");
  assert.ok(!homeHtml.includes("<span>Discover Destinations</span>"), "Must NOT have 'Discover Destinations' label");

  // Assert destination field contains discover option
  assert.ok(
    homeHtml.includes("✨ Let me discover a destination"),
    "Destination select must contain '✨ Let me discover a destination' option"
  );

  // Assert helper text explains both options
  assert.ok(
    homeHtml.includes("Select a destination to search packages directly"),
    "Helper text must explain selecting a destination to search packages directly"
  );
  assert.ok(
    homeHtml.includes("Let me discover a destination"),
    "Helper text must mention 'Let me discover a destination' for destination suggestions"
  );
  console.log("✓ Homepage UI layout verified: Single button, proper select options, and clear helper text.");

  // 2. Verify Flow A: Destination selected -> /packages with destination_id
  console.log("\n=== Verifying Flow A: Destination Selected -> Package Results ===");
  // Query parameters simulating form submission with destination_id = 1 (Manali)
  const flowAParams = new URLSearchParams({
    starting_city: "Delhi",
    budget: "40000",
    travellers: "2",
    duration_days: "5",
    interest: "Adventure",
    travel_type: "Couple",
    month: "12",
    destination_id: "1",
  });

  const flowAUrl = `${FRONTEND_URL}/packages?${flowAParams.toString()}`;
  const flowARes = await fetch(flowAUrl);
  assert.strictEqual(flowARes.status, 200, "Flow A (/packages) must return 200 OK");
  
  // Verify backend packages API returns packages for destination_id 1
  const backendPkgRes = await fetch(`${BACKEND_URL}/packages?${flowAParams.toString()}`);
  assert.strictEqual(backendPkgRes.status, 200, "Backend packages API must return 200 OK");
  const pkgData = await backendPkgRes.json();
  assert.strictEqual(pkgData.success, true);
  assert.ok(Array.isArray(pkgData.data), "Package results must be an array");
  assert.ok(pkgData.data.length > 0, "Packages must be found for destination_id 1");
  for (const pkg of pkgData.data) {
    assert.strictEqual(pkg.destination.id, 1, `Package ${pkg.id} must belong to destination 1`);
  }
  console.log(`✓ Flow A verified: /packages returned ${pkgData.data.length} packages for destination 1 (Manali).`);

  // 3. Verify Flow B: Discover option selected -> /discover
  console.log("\n=== Verifying Flow B: 'Let me discover' Selected -> Destination Discovery ===");
  // Query parameters simulating form submission with no destination_id (discover mode)
  const flowBParams = new URLSearchParams({
    starting_city: "Delhi",
    budget: "40000",
    travellers: "2",
    duration_days: "5",
    interest: "Adventure",
    travel_type: "Couple",
    month: "12",
  });

  const flowBUrl = `${FRONTEND_URL}/discover?${flowBParams.toString()}`;
  const flowBRes = await fetch(flowBUrl);
  assert.strictEqual(flowBRes.status, 200, "Flow B (/discover) must return 200 OK");

  // Verify backend destinations discover API returns scored recommendations
  const backendDiscoverRes = await fetch(`${BACKEND_URL}/discover/destinations?${flowBParams.toString()}`);
  assert.strictEqual(backendDiscoverRes.status, 200, "Backend discover API must return 200 OK");
  const discoverData = await backendDiscoverRes.json();
  assert.strictEqual(discoverData.success, true);
  assert.ok(Array.isArray(discoverData.data), "Discovered destinations must be an array");
  assert.ok(discoverData.data.length > 0, "Discovered destinations must have recommendations");
  console.log(`✓ Flow B verified: /discover returned ${discoverData.data.length} destination recommendations.`);

  console.log("\n=======================================================");
  console.log("ALL SEARCH FLOW UX TESTS PASSED (FLOW A & FLOW B)!");
  console.log("=======================================================");
}

verifySearchFlowUX().catch((err) => {
  console.error("Test failed:", err);
  process.exit(1);
});
