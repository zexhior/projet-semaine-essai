"use strict";

const mockData = [
  {
    nom: "Jean Dupont",
    prenom: "Jean",
    region: "Île-de-France",
    ville: "Paris",
    numero: "0123456789",
  },
  {
    nom: "Marie Martin",
    prenom: "Marie",
    region: "Auvergne-Rhône-Alpes",
    ville: "Lyon",
    numero: "0612456781",
  },
  {
    nom: "Pierre Bernard",
    prenom: "Pierre",
    region: "Provence-Alpes-Côte d'Azur",
    ville: "Marseille",
    numero: "0623456782",
  },
  {
    nom: "Sophie Petit",
    prenom: "Sophie",
    region: "Hauts-de-France",
    ville: "Lille",
    numero: "0634567893",
  },
  {
    nom: "Lucas Robert",
    prenom: "Lucas",
    region: "Nouvelle-Aquitaine",
    ville: "Bordeaux",
    numero: "0645678914",
  },
  {
    nom: "Camille Richard",
    prenom: "Camille",
    region: "Occitanie",
    ville: "Toulouse",
    numero: "0656789125",
  },
  {
    nom: "Thomas Durand",
    prenom: "Thomas",
    region: "Grand Est",
    ville: "Strasbourg",
    numero: "0667891236",
  },
  {
    nom: "Julie Leroy",
    prenom: "Julie",
    region: "Bretagne",
    ville: "Rennes",
    numero: "0678912347",
  },
  {
    nom: "Nicolas Moreau",
    prenom: "Nicolas",
    region: "Pays de la Loire",
    ville: "Nantes",
    numero: "0689123458",
  },
  {
    nom: "Laura Simon",
    prenom: "Laura",
    region: "Normandie",
    ville: "Rouen",
    numero: "0691234569",
  },
  {
    nom: "Hugo Laurent",
    prenom: "Hugo",
    region: "Bourgogne-Franche-Comté",
    ville: "Dijon",
    numero: "0612345670",
  },
  {
    nom: "Emma Michel",
    prenom: "Emma",
    region: "Centre-Val de Loire",
    ville: "Orléans",
    numero: "0621345671",
  },
  {
    nom: "Antoine Garcia",
    prenom: "Antoine",
    region: "Île-de-France",
    ville: "Versailles",
    numero: "0632345672",
  },
  {
    nom: "Chloé David",
    prenom: "Chloé",
    region: "Auvergne-Rhône-Alpes",
    ville: "Grenoble",
    numero: "0643345673",
  },
  {
    nom: "Maxime Roux",
    prenom: "Maxime",
    region: "Occitanie",
    ville: "Montpellier",
    numero: "0654345674",
  },
  {
    nom: "Sarah Fournier",
    prenom: "Sarah",
    region: "Provence-Alpes-Côte d'Azur",
    ville: "Nice",
    numero: "0665345675",
  },
  {
    nom: "Alexandre Girard",
    prenom: "Alexandre",
    region: "Grand Est",
    ville: "Nancy",
    numero: "0676345676",
  },
  {
    nom: "Léa Bonnet",
    prenom: "Léa",
    region: "Nouvelle-Aquitaine",
    ville: "Poitiers",
    numero: "0687345677",
  },
  {
    nom: "Julien Lambert",
    prenom: "Julien",
    region: "Bretagne",
    ville: "Brest",
    numero: "0698345678",
  },
  {
    nom: "Manon Fontaine",
    prenom: "Manon",
    region: "Normandie",
    ville: "Caen",
    numero: "0619345679",
  },
  {
    nom: "Romain Chevalier",
    prenom: "Romain",
    region: "Hauts-de-France",
    ville: "Amiens",
    numero: "0629345680",
  },
  {
    nom: "Elise Robin",
    prenom: "Elise",
    region: "Pays de la Loire",
    ville: "Angers",
    numero: "0639345681",
  },
  {
    nom: "Benoît Masson",
    prenom: "Benoît",
    region: "Bourgogne-Franche-Comté",
    ville: "Besançon",
    numero: "0649345682",
  },
  {
    nom: "Inès Henry",
    prenom: "Inès",
    region: "Centre-Val de Loire",
    ville: "Tours",
    numero: "0659345683",
  },
  {
    nom: "Kevin Renaud",
    prenom: "Kevin",
    region: "Île-de-France",
    ville: "Nanterre",
    numero: "0669345684",
  },
  {
    nom: "Amandine Picard",
    prenom: "Amandine",
    region: "Grand Est",
    ville: "Reims",
    numero: "0679345685",
  },
  {
    nom: "Yanis Collet",
    prenom: "Yanis",
    region: "Auvergne-Rhône-Alpes",
    ville: "Clermont-Ferrand",
    numero: "0689345686",
  },
  {
    nom: "Pauline Noel",
    prenom: "Pauline",
    region: "Occitanie",
    ville: "Nîmes",
    numero: "0699345687",
  },
  {
    nom: "Damien Perrot",
    prenom: "Damien",
    region: "Provence-Alpes-Côte d'Azur",
    ville: "Toulon",
    numero: "0619445688",
  },
  {
    nom: "Clara Legrand",
    prenom: "Clara",
    region: "Nouvelle-Aquitaine",
    ville: "Limoges",
    numero: "0629445689",
  },
  {
    nom: "Adrien Gauthier",
    prenom: "Adrien",
    region: "Bretagne",
    ville: "Quimper",
    numero: "0639445690",
  },
  {
    nom: "Mélanie Philippe",
    prenom: "Mélanie",
    region: "Normandie",
    ville: "Le Havre",
    numero: "0649445691",
  },
  {
    nom: "Quentin Tessier",
    prenom: "Quentin",
    region: "Hauts-de-France",
    ville: "Calais",
    numero: "0659445692",
  },
  {
    nom: "Océane Millet",
    prenom: "Océane",
    region: "Pays de la Loire",
    ville: "Le Mans",
    numero: "0669445693",
  },
  {
    nom: "Florian Marchand",
    prenom: "Florian",
    region: "Bourgogne-Franche-Comté",
    ville: "Chalon-sur-Saône",
    numero: "0679445694",
  },
  {
    nom: "Anaïs Guerin",
    prenom: "Anaïs",
    region: "Centre-Val de Loire",
    ville: "Blois",
    numero: "0689445695",
  },
];

const mock2Toi = [
  {
    agent: "Grossiste",
    msisdn: "0347590003",
  },
  {
    agent: "Distributeur",
    msisdn: "0347590004",
  },
  {
    agent: "Revendeur",
    msisdn: "0347590005",
  },
  {
    agent: "Kiosque",
    msisdn: "0347590006",
  },
  {
    agent: "Boutique",
    msisdn: "0347590007",
  },
  {
    agent: "Partenaire",
    msisdn: "0347590008",
  },
  {
    agent: "Grossiste",
    msisdn: "0347590009",
  },
  {
    agent: "Distributeur",
    msisdn: "0347590010",
  },
  {
    agent: "Revendeur",
    msisdn: "0347590011",
  },
  {
    agent: "Kiosque",
    msisdn: "0347590012",
  },
  {
    agent: "Boutique",
    msisdn: "0347590013",
  },
  {
    agent: "Partenaire",
    msisdn: "0347590014",
  },
  {
    agent: "Grossiste",
    msisdn: "0347590015",
  },
  {
    agent: "Distributeur",
    msisdn: "0347590016",
  },
  {
    agent: "Revendeur",
    msisdn: "0347590017",
  },
  {
    agent: "Kiosque",
    msisdn: "0347590018",
  },
  {
    agent: "Boutique",
    msisdn: "0347590019",
  },
  {
    agent: "Partenaire",
    msisdn: "0347590020",
  },
  {
    agent: "Grossiste",
    msisdn: "0347590021",
  },
  {
    agent: "Distributeur",
    msisdn: "0347590022",
  },
  {
    agent: "Revendeur",
    msisdn: "0347590023",
  },
  {
    agent: "Kiosque",
    msisdn: "0347590024",
  },
  {
    agent: "Boutique",
    msisdn: "0347590025",
  },
  {
    agent: "Partenaire",
    msisdn: "0347590026",
  },
  {
    agent: "Grossiste",
    msisdn: "0347590027",
  },
  {
    agent: "Distributeur",
    msisdn: "0347590028",
  },
  {
    agent: "Revendeur",
    msisdn: "0347590029",
  },
  {
    agent: "Kiosque",
    msisdn: "0347590030",
  },
  {
    agent: "Boutique",
    msisdn: "0347590031",
  },
  {
    agent: "Partenaire",
    msisdn: "0347590032",
  },
  {
    agent: "Grossiste",
    msisdn: "0347590033",
  },
  {
    agent: "Distributeur",
    msisdn: "0347590034",
  },
  {
    agent: "Revendeur",
    msisdn: "0347590035",
  },
  {
    agent: "Kiosque",
    msisdn: "0347590036",
  },
  {
    agent: "Boutique",
    msisdn: "0347590037",
  },
  {
    agent: "Partenaire",
    msisdn: "0347590038",
  },
  {
    agent: "Grossiste",
    msisdn: "0347590039",
  },
  {
    agent: "Distributeur",
    msisdn: "0347590040",
  },
  {
    agent: "Revendeur",
    msisdn: "0347590041",
  },
  {
    agent: "Kiosque",
    msisdn: "0347590042",
  },
];

const userTableBody = document.getElementById("user-table-body");
const twoToiTableBody = document.getElementById("two-toi-table-body");
const userPaginationInfo = document.getElementById("user-pagination-info");
const userPrevPageButton = document.getElementById("user-prev-page");
const userNextPageButton = document.getElementById("user-next-page");
const twoToiPaginationInfo = document.getElementById("two-toi-pagination-info");
const twoToiPrevPageButton = document.getElementById("two-toi-prev-page");
const twoToiNextPageButton = document.getElementById("two-toi-next-page");
const listeSemaineSection = document.getElementById("liste-semaine");
const twoToiSection = document.getElementById("section-2toi");
const navListeSemaine = document.getElementById("nav-liste-semaine");
const nav2Toi = document.getElementById("nav-2toi");
const userTableHeaders = document.querySelectorAll("#user-table th[data-sort-key]");
const twoToiTableHeaders = document.querySelectorAll("#two-toi-table th[data-sort-key]");
const PAGE_SIZE = 13;

let userCurrentPage = 1;
let twoToiCurrentPage = 1;
let userSort = { key: null, direction: "asc" };
let twoToiSort = { key: null, direction: "asc" };

const getTotalPages = (items) => Math.max(1, Math.ceil(items.length / PAGE_SIZE));

const compareValues = (valueA, valueB, direction) => {
  const safeA = String(valueA ?? "");
  const safeB = String(valueB ?? "");
  const comparison = safeA.localeCompare(safeB, "fr", { numeric: true, sensitivity: "base" });

  return direction === "asc" ? comparison : -comparison;
};

const getSortedItems = (items, sortState) => {
  if (!sortState.key) {
    return items;
  }

  return [...items].sort((left, right) =>
    compareValues(left[sortState.key], right[sortState.key], sortState.direction)
  );
};

const updateHeaderSortState = (headers, sortState) => {
  headers.forEach((header) => {
    const sortKey = header.dataset.sortKey;
    const isActive = sortKey === sortState.key;
    const originalLabel = header.dataset.originalLabel || header.textContent.trim();
    const isAscending = isActive && sortState.direction === "asc";
    const isDescending = isActive && sortState.direction === "desc";

    const sortIcon = isAscending
      ? `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-3.5 h-3.5 text-indigo-800">
          <path fill-rule="evenodd" d="M10 3.22a.75.75 0 01.53.22l4.25 4.25a.75.75 0 11-1.06 1.06L10.75 5.81v10.97a.75.75 0 01-1.5 0V5.81L6.28 8.75a.75.75 0 11-1.06-1.06l4.25-4.25a.75.75 0 01.53-.22z" clip-rule="evenodd" />
        </svg>`
      : isDescending
      ? `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-3.5 h-3.5 text-indigo-800">
            <path fill-rule="evenodd" d="M10 16.78a.75.75 0 01-.53-.22l-4.25-4.25a.75.75 0 011.06-1.06l2.97 2.94V3.22a.75.75 0 011.5 0v10.97l2.97-2.94a.75.75 0 111.06 1.06l-4.25 4.25a.75.75 0 01-.53.22z" clip-rule="evenodd" />
          </svg>`
      : `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-3.5 h-3.5 text-slate-500">
            <path fill-rule="evenodd" d="M10 3.22a.75.75 0 01.53.22l4.25 4.25a.75.75 0 11-1.06 1.06L10.75 5.81v10.97a.75.75 0 01-1.5 0V5.81L6.28 8.75a.75.75 0 11-1.06-1.06l4.25-4.25a.75.75 0 01.53-.22zm0 13.56a.75.75 0 01-.53-.22l-4.25-4.25a.75.75 0 011.06-1.06l2.97 2.94V3.22a.75.75 0 011.5 0v10.97l2.97-2.94a.75.75 0 111.06 1.06l-4.25 4.25a.75.75 0 01-.53.22z" clip-rule="evenodd" />
          </svg>`;

    header.dataset.originalLabel = originalLabel;
    header.innerHTML = `<span class="flex justify-between items-center gap-1.5">${originalLabel}${sortIcon}</span>`;
    header.style.cursor = "pointer";
    header.setAttribute(
      "aria-sort",
      isActive ? (sortState.direction === "asc" ? "ascending" : "descending") : "none"
    );
  });
};

const renderUserTable = () => {
  if (!userTableBody || !userPaginationInfo || !userPrevPageButton || !userNextPageButton) {
    return;
  }

  const sortedItems = getSortedItems(mockData, userSort);
  const totalPages = getTotalPages(sortedItems);
  userCurrentPage = Math.min(userCurrentPage, totalPages);

  const startIndex = (userCurrentPage - 1) * PAGE_SIZE;
  const pagedItems = sortedItems.slice(startIndex, startIndex + PAGE_SIZE);

  userTableBody.innerHTML = pagedItems
    .map(
      (user) => `
      <tr class="hover:bg-indigo-100 transition-colors">
        <td class="px-6 py-4 text-sm font-medium text-slate-900 whitespace-nowrap">${user.nom}</td>
        <td class="px-6 py-4 text-sm text-slate-800 whitespace-nowrap">${user.prenom}</td>
        <td class="px-6 py-4 text-sm text-slate-800 whitespace-nowrap">${user.region}</td>
        <td class="px-6 py-4 text-sm text-slate-800 whitespace-nowrap">${user.ville}</td>
        <td class="px-6 py-4 text-sm text-slate-800 whitespace-nowrap">${user.numero}</td>
      </tr>
    `
    )
    .join("");

  userPaginationInfo.textContent = `Page ${userCurrentPage} / ${totalPages}`;
  userPrevPageButton.disabled = userCurrentPage === 1;
  userNextPageButton.disabled = userCurrentPage === totalPages;
  updateHeaderSortState(userTableHeaders, userSort);
};

const renderTwoToiTable = () => {
  if (!twoToiTableBody || !twoToiPaginationInfo || !twoToiPrevPageButton || !twoToiNextPageButton) {
    return;
  }

  const sortedItems = getSortedItems(mock2Toi, twoToiSort);
  const totalPages = getTotalPages(sortedItems);
  twoToiCurrentPage = Math.min(twoToiCurrentPage, totalPages);

  const startIndex = (twoToiCurrentPage - 1) * PAGE_SIZE;
  const pagedItems = sortedItems.slice(startIndex, startIndex + PAGE_SIZE);

  twoToiTableBody.innerHTML = pagedItems
    .map(
      (item) => `
      <tr class="hover:bg-violet-100 transition-colors">
        <td class="px-6 py-4 text-sm font-medium text-slate-900 whitespace-nowrap">${item.agent}</td>
        <td class="px-6 py-4 text-sm text-slate-800 whitespace-nowrap">${item.msisdn}</td>
      </tr>
    `
    )
    .join("");

  twoToiPaginationInfo.textContent = `Page ${twoToiCurrentPage} / ${totalPages}`;
  twoToiPrevPageButton.disabled = twoToiCurrentPage === 1;
  twoToiNextPageButton.disabled = twoToiCurrentPage === totalPages;
  updateHeaderSortState(twoToiTableHeaders, twoToiSort);
};

const toggleSortDirection = (currentSort, key) => {
  if (currentSort.key === key) {
    return {
      key,
      direction: currentSort.direction === "asc" ? "desc" : "asc",
    };
  }

  return {
    key,
    direction: "asc",
  };
};

if (userPrevPageButton && userNextPageButton) {
  userPrevPageButton.addEventListener("click", () => {
    if (userCurrentPage > 1) {
      userCurrentPage -= 1;
      renderUserTable();
    }
  });

  userNextPageButton.addEventListener("click", () => {
    if (userCurrentPage < getTotalPages(mockData)) {
      userCurrentPage += 1;
      renderUserTable();
    }
  });
}

if (twoToiPrevPageButton && twoToiNextPageButton) {
  twoToiPrevPageButton.addEventListener("click", () => {
    if (twoToiCurrentPage > 1) {
      twoToiCurrentPage -= 1;
      renderTwoToiTable();
    }
  });

  twoToiNextPageButton.addEventListener("click", () => {
    if (twoToiCurrentPage < getTotalPages(mock2Toi)) {
      twoToiCurrentPage += 1;
      renderTwoToiTable();
    }
  });
}

if (userTableHeaders.length > 0) {
  userTableHeaders.forEach((header) => {
    header.addEventListener("click", () => {
      const { sortKey } = header.dataset;

      if (!sortKey) {
        return;
      }

      userSort = toggleSortDirection(userSort, sortKey);
      userCurrentPage = 1;
      renderUserTable();
    });
  });
}

if (twoToiTableHeaders.length > 0) {
  twoToiTableHeaders.forEach((header) => {
    header.addEventListener("click", () => {
      const { sortKey } = header.dataset;

      if (!sortKey) {
        return;
      }

      twoToiSort = toggleSortDirection(twoToiSort, sortKey);
      twoToiCurrentPage = 1;
      renderTwoToiTable();
    });
  });
}

renderUserTable();
renderTwoToiTable();

if (listeSemaineSection && twoToiSection && navListeSemaine && nav2Toi) {
  const navActiveClasses = [
    "bg-indigo-900",
    "text-white",
    "border-indigo-900",
    "hover:bg-indigo-950",
  ];
  const navInactiveClasses = ["bg-white/5", "text-white", "border-white/20", "hover:bg-white/10"];

  const setNavState = (button, isActive) => {
    button.classList.remove(...navActiveClasses, ...navInactiveClasses);
    button.classList.add(...(isActive ? navActiveClasses : navInactiveClasses));
  };

  const setActiveSection = (section) => {
    const showListeSemaine = section === "liste-semaine";

    listeSemaineSection.classList.toggle("hidden", !showListeSemaine);
    twoToiSection.classList.toggle("hidden", showListeSemaine);

    setNavState(navListeSemaine, showListeSemaine);
    setNavState(nav2Toi, !showListeSemaine);
  };

  navListeSemaine.addEventListener("click", (event) => {
    event.preventDefault();
    setActiveSection("liste-semaine");
  });

  nav2Toi.addEventListener("click", (event) => {
    event.preventDefault();
    setActiveSection("2toi");
  });

  setActiveSection("liste-semaine");
}
