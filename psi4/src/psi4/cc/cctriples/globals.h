/*
 * @BEGIN LICENSE
 *
 * Psi4: an open-source quantum chemistry software package
 *
 * Copyright (c) 2007-2022 The Psi4 Developers.
 *
 * The copyrights for code used from other parties are included in
 * the corresponding files.
 *
 * This file is part of Psi4.
 *
 * Psi4 is free software; you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, version 3.
 *
 * Psi4 is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License along
 * with Psi4; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
 *
 * @END LICENSE
 */

#ifndef CCTRIPLES_GLOBALS_H  
#define CCTRIPLES_GLOBALS_H  

/*! \file
    \ingroup CCTRIPLES
    \brief Enter brief description of file here
*/
#include <cstdio>
#include "psi4/psifiles.h"
#include "psi4/libdpd/dpd.h"
#include "psi4/libciomr/libciomr.h"
#include "psi4/libpsio/psio.h"

namespace psi {

namespace cctriples {

/* Global variables */
#ifdef EXTERN
#undef EXTERN
#define EXTERN extern
#else
#define EXTERN
#endif

EXTERN struct MOInfo moinfo;
EXTERN struct Params params;
}
}  // namespace psi
#endif
